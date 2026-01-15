from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import git


@csrf_exempt
def update(request):
    """
    Atualiza o código do projeto no PythonAnywhere via git pull.
    Use apenas para deploy manual.
    """
    if request.method == "POST":
        try:
            repo = git.Repo('/home/wimer22/bookstore')
            origin = repo.remotes.origin
            origin.pull()

            return JsonResponse(
                {"status": "success", "message": "Código atualizado com sucesso"}
            )
        except Exception as e:
            return JsonResponse(
                {"status": "error", "message": str(e)},
                status=500
            )

    return JsonResponse(
        {"status": "error", "message": "Método não permitido"},
        status=405
    )


def hello_world(request):
    """
    View simples para teste do deploy
    """
    return render(request, 'hello_world.html')
