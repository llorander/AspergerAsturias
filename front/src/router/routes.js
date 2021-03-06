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
    path: "/registration",
    component: () => import("@/views/Home/RegistrationPage.vue"),
  },
  {
    path: "/login",
    component: () => import("@/views/Home/LoginPage.vue"),
  },
  {
    path: "/user-menu",
    component: () => import("@/views/User/UserMenu.vue"),
  },
  {
    path: "/task-list",
    component: () => import("@/views/User/TaskList.vue"),
  },
  {
    path: "/admin-menu",
    component: () => import("@/views/Admin/AdminMenu.vue"),
  },
  {
    path: "/admin-total-points",
    component: () => import("@/views/Admin/TotalPointsPage.vue"),
  },
  {
    path: "/add-reward",
    component: () => import("@/views/Admin/AddRewardPage.vue"),
  },
  {
    path: "/admin-rewards-list",
    component: () => import("@/views/Admin/AdminRewardsList.vue"),
  },
  {
    path: "/admin-planning",
    component: () => import("@/views/Admin/AdminPlanningPage.vue"),
  },
  {
    path: "/admin-total-points",
    component: () => import("@/views/Admin/TotalPointsPage.vue"),
  },
];
