export const routes = [
  {
    path: "/",
    component: () => import("@/views/Home/HomePage.vue"),
  },
  {
    path: "/admin-panel",
    component: () => import("@/views/Admin/AdminPanel.vue"),
  },
  {
    path: "/tasks",
    component: () => import("@/views/TaskList/TaskListPage.vue"),
  },
];
